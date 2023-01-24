from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, IPvAnyAddress, conint

class ProcessStatus(str, Enum):
    STARTING = 'STARTING',
    RUNNING = 'RUNNING'


class SocketAddress(BaseModel):
    host: IPvAnyAddress = Field(description="the IP address of the socket's host")
    port: conint(ge=0, le=65535) = Field(description="the socket's port number")
    is_public: bool = Field(False, description='if true, the socket is publicly accessible')


class ProcessInfo(BaseModel):
    """
    Information about a running process.
    """
    process_name: str = Field(description="the name of the process")
    group: Optional[str] = Field(None, description="the group to which the process belongs, if any")

    # A list of host/port pairs that the process exposes
    socket_addresses: List[SocketAddress] = Field(
        description='a list of socket addresses that the process is exposing'
    )

    created: datetime = Field(description='the date and time when the process was launched')

    status: ProcessStatus = Field(description="the status of the process - is the process running, or has the process started but is not running yet?")
