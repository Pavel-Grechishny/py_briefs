## Наблюдатель ##

> Поведенческий

```python
"""Демонстратор наблюдателя: упрощенно."""

class Camera:
    """Камера видеонаблюдения."""
    id_ = 0
    
    def __init__(self, name: str):
        self.id = self.__class__.id_
        self.__class__.id_ += 1
        self.name = name

    def __hash__(self):
        return self.id

    def make_photo(self):
        """Реакция наблюдателя на событие."""
        print(f'фото с камеры {self.name}')

# >>> camera_1 = Camera('c1')
# >>> Camera.id_
# 1
# >>> camera_2 = Camera('c2')
# >>> Camera.id_
# 2
# >>> camera_1.__hash__()
# 0
# >>> camera_2.__hash__()
# 1
# >>> camera_1.make_photo()
# фото с камеры c1
# >>> camera_2.make_photo()
# фото с камеры c2


class CameraSystem:
    """Пост управления камерами."""
    def __init__(self):
        self.cameras: set[Camera] = set()

    def connect(self, camera: Camera):
        """Подключает камеру к посту. (Подписка экземпляра наблюдателя)"""
        self.cameras.add(camera)

    def disconnect(self, camera: Camera):
        """Отключает камеру от поста. (Отмена подписки экземпляра наблюдателя)"""
        self.cameras.remove(camera)

    def notify(self):
        """Отправляет сигнал всем камерам (наблюдателям)"""
        for camera in self.cameras:
            camera.make_photo()


# >>> system_post = CameraSystem()
# >>>
# >>> camera_1 = Camera('c1')
# >>> camera_2 = Camera('c2')
# >>> camera_3 = Camera('c3')
# >>> camera_4 = Camera('c4')
# >>>
# >>> system_post.connect(camera_1)
# >>> system_post.connect(camera_2)
# >>> system_post.connect(camera_3)
# >>> system_post.connect(camera_4)
# >>>
# >>> # происходит событие
# >>>
# >>> system_post.notify()
# фото с камеры c1
# фото с камеры c2
# фото с камеры c3
# фото с камеры c4
# >>>
# >>> system_post.disconnect(camera_4)
# >>>
# >>> # происходит событие
# >>> system_post.notify()
# фото с камеры c1
# фото с камеры c2
# фото с камеры c3
```

