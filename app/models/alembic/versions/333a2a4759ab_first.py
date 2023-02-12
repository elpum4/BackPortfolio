"""first

Revision ID: 333a2a4759ab
Revises: 
Create Date: 2023-02-11 18:37:22.612591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333a2a4759ab'
down_revision = None
branch_labels = None
depends_on = None


from alembic import context


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('educacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ed_actual', sa.Boolean(), nullable=True),
    sa.Column('ed_comienzo', sa.DateTime(), nullable=True),
    sa.Column('ed_descripcion', sa.String(length=1000), nullable=True),
    sa.Column('ed_final', sa.DateTime(), nullable=True),
    sa.Column('ed_institucion', sa.String(length=100), nullable=True),
    sa.Column('ed_titulo', sa.String(length=100), nullable=True),
    sa.Column('ed_urllogo', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_educacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experiencia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exp_actual', sa.Boolean(), nullable=True),
    sa.Column('exp_comienzo', sa.DateTime(), nullable=True),
    sa.Column('exp_descripcion', sa.String(length=1000), nullable=True),
    sa.Column('exp_final', sa.DateTime(), nullable=True),
    sa.Column('exp_sitio', sa.String(length=100), nullable=True),
    sa.Column('exp_titulo', sa.String(length=100), nullable=True),
    sa.Column('exp_urllogo', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_experiencia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hd_mail', sa.String(length=50), nullable=True),
    sa.Column('hd_profesion', sa.String(length=50), nullable=True),
    sa.Column('hd_sobremi', sa.String(length=1000), nullable=True),
    sa.Column('hd_urlbanner', sa.String(length=1000), nullable=True),
    sa.Column('hd_urlgit', sa.String(length=1000), nullable=True),
    sa.Column('hd_urllkd', sa.String(length=1000), nullable=True),
    sa.Column('hd_urlperfil', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proyecto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proy_cliente', sa.String(length=100), nullable=True),
    sa.Column('proy_descripcion', sa.String(length=1000), nullable=True),
    sa.Column('proy_titulo', sa.String(length=100), nullable=True),
    sa.Column('proy_url', sa.String(length=1000), nullable=True),
    sa.Column('proy_urlimg', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_proyecto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sk_titulo', sa.String(length=50), nullable=True),
    sa.Column('sk_habilidad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('skill')
    op.drop_table('tipo_proyecto')
    op.drop_table('proyecto')
    op.drop_table('profile')
    op.drop_table('tipo_experiencia')
    op.drop_table('experiencia')
    op.drop_table('tipo_educacion')
    op.drop_table('educacion')
    # ### end Alembic commands ###


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass