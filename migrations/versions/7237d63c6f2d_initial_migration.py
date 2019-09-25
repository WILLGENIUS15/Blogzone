"""Initial Migration

Revision ID: 7237d63c6f2d
Revises: 
Create Date: 2019-09-24 16:18:23.475888

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7237d63c6f2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('blogs', sa.Column('blog_content', sa.String(length=8000), nullable=True))
    op.add_column('blogs', sa.Column('blog_title', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('dislikes', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('likes', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('posted', sa.DateTime(), nullable=True))
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('username', sa.String(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'body')
    op.add_column('comments', sa.Column('blog', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'blogs', ['blog'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'username')
    op.drop_column('comments', 'email')
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'blog_id')
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('firstname', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('lastname', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.drop_column('users', 'about')
    op.drop_column('users', 'occupation')
    op.drop_column('users', 'profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('occupation', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('about', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'lastname')
    op.drop_column('users', 'firstname')
    op.drop_column('users', 'bio')
    op.add_column('comments', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'blog')
    op.add_column('blogs', sa.Column('body', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'username')
    op.drop_column('blogs', 'user_id')
    op.drop_column('blogs', 'posted')
    op.drop_column('blogs', 'likes')
    op.drop_column('blogs', 'dislikes')
    op.drop_column('blogs', 'blog_title')
    op.drop_column('blogs', 'blog_content')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
