"""This Module contains needed mappers to make scalable the controllers.

    Remember update SQL_TABLES and ALEMBIC_TARGET_METADATA_LIST when a new model 
    has been inserted.
"""
from typing import List, Optional, Text


from app.models.bases import (
    educacion,
    experiencia,
    profile,
    proyecto,
    skill,
    users,
)

ALEMBIC_TARGET_METADATA_LIST = [
    educacion.Educacion.metadata,
    experiencia.Experiencia.metadata,
    profile.Profile.metadata,
    proyecto.Proyecto.metadata,
    skill.Skill.metadata,
    users.Users.metadata,
]
