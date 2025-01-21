'''
version check and update
'''

from enum import Enum, auto
from dataclasses import dataclass

from github import Github
from github.GitRelease import GitRelease
from github.GithubException import (
    GithubException,
    UnknownObjectException,
    RateLimitExceededException
)


__version__: str = "v0.0.0"  # todo: adjust this version for release
repo_id_for_testing: int = 373494377  # todo: remove this
THIS_REPO_ID: int = 919969264
'''
the repo-id can be determined using the github api
repo by name: https://api.github.com/repos/EchterTimo/PyPasswordTool
repo by id: https://api.github.com/repositories/919969264
'''


class VersionStatus(Enum):
    """
    Enum representing the status of the software version.
    """
    PRE_RELEASE = auto()
    '''A version that is not finalized or generally available.'''

    LATEST = auto()
    '''The most recent and up-to-date version.'''

    OUTDATED = auto()
    '''An older version that is no longer the latest.'''

    UNKNOWN = auto()
    '''A version status that cannot be determined.'''


@dataclass
class VersionDetails:
    '''
    Abstraction for version status, comparing and status
    '''

    current_version: str
    latest_version_release: GitRelease | None
    fetch_error: GithubException = None

    @property
    def latest_version(self) -> str:
        '''
        Get the latest version
        '''
        if self.latest_version_release:
            return self.latest_version_release.title

    @property
    def version_status(self) -> VersionStatus:
        '''
        current version status
        '''
        return determine_version_status(
            self.current_version, self.latest_version)

    @classmethod
    def get(cls, repo_id: int = THIS_REPO_ID):
        '''
        Get a VersionDetails instance for the current software.
        '''
        r, e = get_latest_release_and_error(repo_id)
        return VersionDetails(
            current_version=__version__,
            latest_version_release=r,
            fetch_error=e
        )

    # def __repr__(self) -> str:
        # return VersionDetails(current_version='v0.0.0', latest_version_release=GitRelease(title="v1.2.1"), fetch_error=None)
        # todo: edit __repr__ method


def get_latest_release_and_error(
    repo_id: int
) -> tuple[GitRelease, GithubException]:
    '''
    Get the latest release as a object
    '''
    try:
        g = Github(timeout=3, retry=0)
        repo = g.get_repo(repo_id)
        return repo.get_latest_release(), None
    except UnknownObjectException as e:
        return None, e
    except RateLimitExceededException as e:
        return None, e
    except Exception as e:
        print("Error: Unexpected Exception while retrieving Repo data")
        print(e)
        return None, e


def determine_version_status(
    user_version: str,
    latest_version: str
) -> VersionStatus:
    """
    Determine the status of a given version compared to the latest version.
    the format should
    """
    if user_version is None or latest_version is None:
        return VersionStatus.UNKNOWN
    if user_version == latest_version:
        return VersionStatus.LATEST
    elif user_version < latest_version:
        return VersionStatus.OUTDATED
    elif user_version > latest_version:
        return VersionStatus.PRE_RELEASE


if __name__ == '__main__':
    t = VersionDetails.get(repo_id_for_testing)
    if not t.fetch_error:
        print(t)
        print(t.current_version)
        print(t.latest_version)
        print(t.version_status)
    else:
        print(t.fetch_error)

    # todo: implement a way for the user to download the newest version
    # ! manual or automatic?
