from requests import Session
from .constants import RoutePath
from .utils import constructUrl, checkAndRaise 

class MegaSdkRestClient:

	def __init__(self,base_endpoint,session=Session()):
		self.base_endpoint = base_endpoint
		self.session = session

	def login(self, email, password):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_LOGIN), data={
			'email': email,
			'password': password
		}).json()
		return checkAndRaise(res, RoutePath.PATH_LOGIN)

	def addDl(self, link, directory):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_ADD_DL), data={
			'link': link,
			'dir': directory
		}).json()
		return checkAndRaise(res, RoutePath.PATH_ADD_DL)

	def cancelDl(self, gid):
		res = self.session.post(constructUrl(self.base_endpoint, RoutePath.PATH_CANCEL_DL), data={
			'gid': gid
		}).json()
		return checkAndRaise(res, RoutePath.PATH_CANCEL_DL)

	def getDownloadInfo(self, gid):
		res = self.session.get(constructUrl(self.base_endpoint, RoutePath.PATH_DL_INFO.format(gid))).json()
		return checkAndRaise(res, RoutePath.PATH_DL_INFO)

	def ping(self):
		res = self.session.get(constructUrl(self.base_endpoint, RoutePath.PATH_PING)).json()
		return res 

