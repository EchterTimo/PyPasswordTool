'''
version check and update
'''

from enum import Enum, auto
from dataclasses import dataclass

from github import Github
from github.GitRelease import GitRelease
from github.GithubException import (
    UnknownObjectException, RateLimitExceededException
)


__version__: str = "0.0.0"  # todo: adjust this version for release
THIS_REPO_ID: int = 919969264
'''
the repo-id can be determined using the github api
repo by name: https://api.github.com/repos/EchterTimo/PyPasswordTool
repo by id: https://api.github.com/repositories/919969264
'''


class VersionStatus(Enum):
    """
    Enum representing the status of a software version.
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
    abstraction for version status, comparing and status
    '''

    current_version: str
    latest_version: str
    latest_version_release: GitRelease  # todo: last edit

    @property
    def version_status(self) -> VersionStatus:
        '''
        current version status
        '''
        return determine_version_status(
            self.current_version, self.latest_version)


def get_latest_release(repo_id: int) -> GitRelease:
    '''
    Get the latest release as a object
    '''
    try:
        g = Github(timeout=3, retry=0)
        repo = g.get_repo(repo_id)
        return repo.get_latest_release()
    except UnknownObjectException:
        return None
    except RateLimitExceededException:
        return None


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
    pass
