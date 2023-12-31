"""INIT

Revision ID: d5ecaa15f8dd
Revises: 
Create Date: 2023-12-10 19:55:00.135911

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d5ecaa15f8dd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "owners",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("photo_url", sa.String(), nullable=True),
        sa.Column("birthday", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_owners_id"), "owners", ["id"], unique=False)
    op.create_index(op.f("ix_owners_name"), "owners", ["name"], unique=False)
    op.create_table(
        "properties",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("code_internal", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["owners.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_properties_id"), "properties", ["id"], unique=False)
    op.create_index(op.f("ix_properties_name"), "properties", ["name"], unique=False)
    op.create_table(
        "property_images",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("file_url", sa.String(), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("property_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["property_id"],
            ["properties.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_property_images_id"), "property_images", ["id"], unique=False
    )
    op.create_table(
        "property_traces",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date_sale", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=False),
        sa.Column("tax", sa.Integer(), nullable=False),
        sa.Column("property_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["property_id"],
            ["properties.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_property_traces_id"), "property_traces", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_property_traces_name"), "property_traces", ["name"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_property_traces_name"), table_name="property_traces")
    op.drop_index(op.f("ix_property_traces_id"), table_name="property_traces")
    op.drop_table("property_traces")
    op.drop_index(op.f("ix_property_images_id"), table_name="property_images")
    op.drop_table("property_images")
    op.drop_index(op.f("ix_properties_name"), table_name="properties")
    op.drop_index(op.f("ix_properties_id"), table_name="properties")
    op.drop_table("properties")
    op.drop_index(op.f("ix_owners_name"), table_name="owners")
    op.drop_index(op.f("ix_owners_id"), table_name="owners")
    op.drop_table("owners")
    # ### end Alembic commands ###
