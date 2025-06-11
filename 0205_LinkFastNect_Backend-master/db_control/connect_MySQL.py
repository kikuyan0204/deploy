from sqlalchemy import create_engine
import os
from pathlib import Path
from dotenv import load_dotenv

# .envファイルの読み込み（コメントアウトを外す）
base_path = Path(__file__).parents[1]  # backendディレクトリへのパス
env_path = base_path / '.env'  # .env ファイルのパス
load_dotenv(dotenv_path=env_path)  # .env ファイルを読み込む

# データベース接続情報を環境変数から取得
DB_USER = os.getenv('DB_USER')  # tech0gen10student
DB_PASSWORD = os.getenv('DB_PASSWORD')  # vY7JZNfU
DB_HOST = os.getenv('DB_HOST')  # rdbs-002-step3-1-oshima3.mysql.database.azure.com
DB_PORT = os.getenv('DB_PORT')  # 3306
DB_NAME = os.getenv('DB_NAME')  # step3-1_kikuyan

# SSL証明書のパス（証明書ファイルが存在するか確認）
ssl_cert = str(base_path / 'DigiCertGlobalRootCA.crt.pem')

# MySQLの接続URLの構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# エンジンの作成（SSL設定を追加）
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ssl_ca": ssl_cert  # SSL証明書を指定
        }
    },
    echo=True,  # SQLのログを表示する（デバッグ用）
    pool_pre_ping=True,  # 接続確認を有効にする（切断された接続を検出）
    pool_recycle=3600  # コネクションプールを1時間ごとに再接続
)

# 現在の作業ディレクトリと証明書ファイルの存在確認を表示
print("Current working directory:", os.getcwd())
print("Certificate file exists:", os.path.exists(ssl_cert))  # 証明書が存在するか確認
