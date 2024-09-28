import os

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

    # Validação simples para garantir que as variáveis estão sendo carregadas
    assert os.getenv("CLIENT_ID") is not None, "CLIENT_ID não foi carregado"
    assert os.getenv("CLIENT_SECRET") is not None, "CLIENT_SECRET não foi carregado"
    assert os.getenv("CLIENT_AGENT") is not None, "CLIENT_AGENT não foi carregado"
