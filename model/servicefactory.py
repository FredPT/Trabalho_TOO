from model.service import Service
from model.corte_masculino import CorteMasculino
from model.corte_feminino import CorteFeminino
from model.barba import Barba
from model.pintar_cabelo import PintarCabelo
from model.sobrancelha import Sobrancelha

class ServiceFactory:
    @staticmethod
    def criarServico(tipo):
        # Dicionário de serviços
        servicos = {
            "CorteM": CorteMasculino(),
            "CorteF": CorteFeminino(),
            "Barba": Barba(),
            "Pintar": PintarCabelo(),
            "Sobrancelha": Sobrancelha()
        }
        return servicos.get(tipo, Service("Serviço Padrão", 30, 30.0))