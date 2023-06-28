from src.events import Event


def test_can_instantiate() -> None:
    # given
    instance = Event()

    # then
    assert isinstance(instance, Event)