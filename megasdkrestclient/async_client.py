from aiohttp import ClientSession
from. constants import RoutePath
from .utils import constructUrl, checkAndRaise

class AsyncMegaSdkRestClient:

    def __init__(self, base_endpoint, session=ClientSession()):
        self.base_endpoint = base_endpoint
        self.session = session

    async def login(self, email, password):
        async with self.session.post(constructUrl(self.base_endpoint,RoutePath.PATH_LOGIN),data={
            'email': email,
            'password': password
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, RoutePath.PATH_LOGIN)
        
    async def addDl(self, link, directory):
        async with self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_ADD_DL),data={
            'link': link,
            'dir': directory
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, RoutePath.PATH_ADD_DL)
    
    async def cancelDl(self, gid):
        async with self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_CANCEL_DL),data={
            'gid': gid
        }) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, RoutePath.PATH_CANCEL_DL)

    async def getDownloadInfo(self, gid):
        async with self.session.get(constructUrl(self.base_endpoint, RoutePath.PATH_DL_INFO.format(gid))) as res:
            res_json = await res.json()
            return checkAndRaise(res_json, RoutePath.PATH_DL_INFO)

    async def ping(self):
        async with self.session.get(constructUrl(self.base_endpoint, RoutePath.PATH_PING)) as res:
            return await res.json()
