import rdflib, sqlite3


class creator():


	def __init__(self,name):
		self.con = sqlite3.connect(name)
		self.c = self.con.cursor()

		self.c.execute("create table URIs (URIPredicate string, StringPredicate string, URIObject string, StringObject string)")
		self.c.execute("create table Strings (URIPredicate string, StringPredicate string, StringObject string)")
		self.c.execute("create table InternalURIs (URIPredicate string, StringPredicate string, InternalURIObject string, StringObject string)")
		self.con.commit()

        @staticmethod
        def exampleURLs():
		print "http://dbpedia.org/resource/Pittsburgh"
		print "URLs from the Semantic Web"
		print "check out http://wiki.dbpedia.org/"

	def getData(self,myUrl):
		g = rdflib.Graph()
		g.load(myUrl)
		myData = []
		for subject,pred,obj in g:
		        temp = [subject,pred,obj]
		        myData.append(temp)
		return myData

	def processData(self,myData):
		Names = []
		for el in myData:
		        nameA = el[0].split("/")
		        name1 = nameA[len(nameA)-1]
		        nameB = el[1].split("/")
	        	name2 = nameB[len(nameB)-1]
		        nameC = el[2].split("/")
		        name3 = nameC[len(nameC)-1]
		        temp = [name1, el[0], name2, el[1], name3, el[2] ]
		        Names.append(temp)
		return Names

	def storeData(self,processedData, subject):

		for N in processedData:
		        if(N[0] == subject):
		                N[2] = N[2].replace("'","")
		                N[3] = N[3].replace("'","")
		                N[4] = N[4].replace("'","")
		                N[5] = N[5].replace("'","")
				try:
			                if(N[5].find("http:")>=0):
			                        query = "insert into URIs values('"+N[3]+"','"+N[2]+"','"+N[5]+"','"+N[4]+"')"
			                else:
			                        query = "insert into Strings values ('"+N[3]+"','"+N[2]+"','"+N[5]+"')"
			                self.c.execute(query)
					self.con.commit()
					return True
				except:
					return False

