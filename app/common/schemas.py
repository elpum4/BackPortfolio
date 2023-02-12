"""This module contains the main schemas for Features API

The schemas represented in this module are used (in the most cases) to validate
the input data request that receives the API.
"""
from marshmallow import Schema, fields


class EducacionSchema(Schema):

    id = fields.Integer()
    ed_actual = fields.Boolean()
    ed_comienzo = fields.DateTime()
    ed_descripcion = fields.String()
    ed_final = fields.DateTime()
    ed_institucion = fields.String()
    ed_titulo = fields.String()
    ed_urllogo = fields.String()
    ed_tipo = fields.Integer()


class ExperienciaSchema(Schema):

    id = fields.Integer()
    exp_actual = fields.Boolean()
    exp_comienzo = fields.DateTime()
    exp_descripcion = fields.String()
    exp_final = fields.DateTime()
    exp_sitio = fields.String()
    exp_titulo = fields.String()
    ex_urllogo = fields.String()
    exp_tipo = fields.Integer()


class ProfileSchema(Schema):

    id = fields.Integer()
    hd_mail = fields.String()
    hd_profesion = fields.String()
    hd_sobremi = fields.String()
    hd_urlbanner = fields.String()
    hd_urlgit = fields.String()
    hd_urllkd = fields.String()
    hd_urlperfil = fields.String()


class ProyectoSchema(Schema):

    id = fields.Integer()
    proy_cliente = fields.String()
    proy_descripcion = fields.DateTime()
    proy_titulo = fields.String()
    proy_url = fields.String()
    proy_urlimg = fields.String()
    proy_categoria = fields.String()


class SkillSchema(Schema):

    __tablename__ = "skill"

    id = fields.Integer()
    sk_titulo = fields.String()
    sk_habilidad = fields.Integer()
