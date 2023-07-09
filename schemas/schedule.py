from pydantic import BaseModel
from model.schedule import Schedule
from typing import Optional, List


class ScheduleSchema(BaseModel):
    """ Define como um novo agendamento a ser inserido deve ser representado
    """
    date: str = '12/07/2023 08:30'
    name: str = "Rex"
    src: Optional[str] = "https://placehold.co/600x400"

class ScheduleViewSchema(BaseModel):
    """ Define como um agendamento será retornado.
    """
    id: int = 1
    name: str = "Rex"
    date: str = '12/07/2023 08:30'
    src: str = "https://placehold.co/600x400"

    
class ScheduleListSearchSchema(BaseModel):
    """ Define os parâmetros de busca da listagem de agendamentos
    """
    date: str = '11/07/2023'

class ScheduleListSchema(BaseModel):
    """ Define como uma listagem de agendamentos será retornada.
    """
    data: List[ScheduleSchema]

def apresenta_agendamentos(agendamentos: List[Schedule]):
    """ Retorna uma representação dos agendamentos seguindo o schema definido em
        ScheduleViewSchema.
    """
    result = []
    for agendamento in agendamentos:
        result.append(apresenta_agendamento(agendamento))

    return {"schedules": result}

def apresenta_agendamento(agendamento: Schedule):
    """ Retorna uma representação do agendamento seguindo o schema definido em
        ScheduleViewSchema.
    """
    date = agendamento.date.strftime("%d/%m/%Y %H:%M")
    return {
            "id": agendamento.id,
            "name": agendamento.name,
            "date": date,
            "src": agendamento.src,
        }