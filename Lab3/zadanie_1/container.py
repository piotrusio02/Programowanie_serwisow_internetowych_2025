from dependency_injector import containers, providers

from repositories.post_repository import PostRepository
from services.post_service import PostService

class Container(containers.DeclarativeContainer):

    repository = providers.Singleton(
        PostRepository,
    )

    service = providers.Factory(
        PostService,
        repository=repository,
    )