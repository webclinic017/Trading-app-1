"""empty message

Revision ID: 9a9a7be125f0
Revises: 
Create Date: 2021-09-29 00:48:56.846295

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9a9a7be125f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crons',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cron_id', sa.String(), nullable=True),
    sa.Column('cron_type', sa.String(), nullable=True),
    sa.Column('cron_on', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('cron_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cron_id')
    )
    op.create_index(op.f('ix_crons_id'), 'crons', ['id'], unique=False)
    op.create_table('stocks',
    sa.Column('unique_id', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('securityType', sa.String(), nullable=True),
    sa.Column('markerSector', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('exchCode', sa.String(), nullable=True),
    sa.Column('shareClassFIGI', sa.String(), nullable=True),
    sa.Column('compositeFIGI', sa.String(), nullable=True),
    sa.Column('securityType2', sa.String(), nullable=True),
    sa.Column('securityDescription', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('unique_id')
    )
    op.create_table('bars_daily',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stock_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('adjusted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.unique_id'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stock_id', 'timestamp')
    )
    op.create_index(op.f('ix_bars_daily_id'), 'bars_daily', ['id'], unique=False)
    op.create_table('bars_hour',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stock_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('adjusted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.unique_id'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stock_id', 'timestamp')
    )
    op.create_index(op.f('ix_bars_hour_id'), 'bars_hour', ['id'], unique=False)
    op.create_table('bars_minute',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stock_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('adjusted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.unique_id'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('stock_id', 'timestamp')
    )
    op.create_index(op.f('ix_bars_minute_id'), 'bars_minute', ['id'], unique=False)
    op.create_table('quotes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stock_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('ask_exchanges', sa.Enum('A', 'B', 'C', 'D', 'E', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', name='exch'), nullable=True),
    sa.Column('ask_price', sa.Float(), nullable=True),
    sa.Column('ask_size', sa.Integer(), nullable=True),
    sa.Column('bid_exchange', sa.Enum('A', 'B', 'C', 'D', 'E', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', name='exch'), nullable=True),
    sa.Column('bid_price', sa.Float(), nullable=True),
    sa.Column('bid_size', sa.Integer(), nullable=True),
    sa.Column('quote_condition', postgresql.ARRAY(sa.String()), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.unique_id'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quotes_id'), 'quotes', ['id'], unique=False)
    op.create_table('trades',
    sa.Column('stock_id', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('exchange', sa.Enum('A', 'B', 'C', 'D', 'E', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', name='exch'), nullable=True),
    sa.Column('trade_price', sa.Float(), nullable=True),
    sa.Column('trade_size', sa.Float(), nullable=True),
    sa.Column('trade_condition', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('trade_id', sa.String(), nullable=True),
    sa.Column('tape', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['stocks.unique_id'], onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trades_id'), 'trades', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trades_id'), table_name='trades')
    op.drop_table('trades')
    op.drop_index(op.f('ix_quotes_id'), table_name='quotes')
    op.drop_table('quotes')
    op.drop_index(op.f('ix_bars_minute_id'), table_name='bars_minute')
    op.drop_table('bars_minute')
    op.drop_index(op.f('ix_bars_hour_id'), table_name='bars_hour')
    op.drop_table('bars_hour')
    op.drop_index(op.f('ix_bars_daily_id'), table_name='bars_daily')
    op.drop_table('bars_daily')
    op.drop_table('stocks')
    op.drop_index(op.f('ix_crons_id'), table_name='crons')
    op.drop_table('crons')
    # ### end Alembic commands ###