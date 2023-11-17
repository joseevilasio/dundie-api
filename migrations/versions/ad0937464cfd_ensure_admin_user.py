"""ensure_admin_user

Revision ID: ad0937464cfd
Revises: 50109d7e02dd
Create Date: 2023-11-15 22:19:15.027508

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from dundie.models.user import User
from sqlmodel import Session

# revision identifiers, used by Alembic.
revision = 'ad0937464cfd'
down_revision = '50109d7e02dd'
branch_labels = None
depends_on = None


def upgrade() -> None:  # NEW
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@dm.com",
        dept="management",
        currency="USD",
        password="admin",  # pyright: ignore
    )
    # if admin user already exists it will raise IntegrityError
    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
