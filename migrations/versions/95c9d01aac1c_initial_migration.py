"""Initial migration

Revision ID: 95c9d01aac1c
Revises: 
Create Date: 2023-05-26 14:28:46.326564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c9d01aac1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('candidate_name', sa.String(length=50), nullable=True),
    sa.Column('candidate_information', sa.Text(), nullable=True),
    sa.Column('candidate_schedule', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('race_name', sa.String(length=50), nullable=True),
    sa.Column('race_information', sa.Text(), nullable=True),
    sa.Column('race_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voter_name', sa.String(length=50), nullable=True),
    sa.Column('voter_information', sa.Text(), nullable=True),
    sa.Column('voter_phone_number', sa.String(length=100), nullable=True),
    sa.Column('voter_profile', sa.JSON(), nullable=True),
    sa.Column('voter_engagement_history', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voter_communication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('twilio_conversation_sid', sa.String(length=50), nullable=True),
    sa.Column('conversation', sa.JSON(), nullable=True),
    sa.Column('communication_type', sa.String(length=50), nullable=True),
    sa.Column('communication_goal', sa.Text(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('candidate_id', sa.Integer(), nullable=True),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.Column('voter_outreach_schedule', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['candidate.id'], ),
    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['voter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voter_communication')
    op.drop_table('voter')
    op.drop_table('race')
    op.drop_table('candidate')
    # ### end Alembic commands ###