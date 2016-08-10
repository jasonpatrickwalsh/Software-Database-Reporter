import sys
import csv
import webbrowser
from difflib import SequenceMatcher

##########################################
##          SoftwareDB Adjuster         ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################


def file_to_list(s0,s1,s2,s3,s4):#where s2 equals what's in column s1 grab repective from column s3 in file s0
	f = open(s0,'rt')
	#print('pulling '+s3+' where '+s1+' is equal to '+s2+' in file '+s0+'...\n\n')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		#print(s0+' is column '+str(compareCol))
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if s4 == "explicit":
				if row[compareCol]==s2:
					rowMatches+=str(count)+','
			if s4 == "similar":
				if similar(row[compareCol],s2) > 0.8:
					rowMatches+=str(count)+','
			if s4 == "contains":
				if s2.find(",") != -1:
					allmatch=True
					multi = s2.split(',')
					for el in multi:
						if row[compareCol].lower().find(str(el).lower()) == -1:
							allmatch=False
					if allmatch == True:
						rowMatches+=str(count)+","
				if row[compareCol].lower().find(s2.lower()) != -1:
					rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#get the relevant column we want to read data from
		count=0
		for row in fileReader:
			for el in row:
				if el == s3:
					readCol = count;
				count+=1
			break
		#print(s2+' is column '+str(readCol))
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on commas
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(count) == str(elem): #if the row# matches an entry in "matches"
					results+=row[0]+','
					results+=row[readCol]+'\n'
			count+=1
		f.seek(0)
		
			
	finally:
		f.close() 
		return results
		
def file_to_full_list(s0,s1,s2):#where s2 equals what's in s1 grab all
	f = open(s0,'rt')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if str(row[compareCol])==s2:
				rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on commas
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(count) == str(elem): #if the row# matches an entry in "matches"
					results+=('|'.join(row))+'\n'
			count+=1
		f.seek(0)
		
			
	finally:
		f.close() 
		return results

def file_to_full_list_from_name(s0,s1,s2,s3,s4):#where s2 equals what's in s1 if name matches s3
	f = open(s0,'rt')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if s4=="explicit":
				if row[compareCol]==s2:
					rowMatches+=str(count)+','
			if s4=="similar":
				if similar(row[compareCol],s2) > 0.8:
					rowMatches+=str(count)+','
			if s4=="contains":
				if s2.find(",") != -1:
					allmatch=True
					multi = s2.split(',')
					for el in multi:
						if row[compareCol].lower().find(str(el).lower()) == -1:
							allmatch=False
					if allmatch==True:
						rowMatches+=str(count)+','
				else:
					if row[compareCol].lower().find(s2.lower()) != -1:
						rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on pipes
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(elem) == str(count) and row[1] == s3: #if the row# matches an entry in "matches"
					results+=('|'.join(row))
			count+=1
		f.seek(0)
			
	finally:
		f.close() 
		return results

def landesk_to_full_list_from_name(s0,s1,s2,s3):#where s2 matches s1 and name is s3
	f = open(s0,'rt')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		name = s3.split(' ')
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		#print(s0+' is column '+str(compareCol))
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if row[compareCol]==s2 and row[1]==name[0] and row[2]==name[1] :
				rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on commas
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(count) == str(elem): #if the row# matches an entry in "matches"
					results='|'.join(row)
			count+=1
		f.seek(0)
		
			
	finally:
		f.close() 
		return results
		
def landesk_to_full_name(s0,s1,s2):
	f = open(s0,'rt')
	#print('pulling all where '+s1+' is equal to '+s2+' in file '+s0+'...\n\n')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		#print(s0+' is column '+str(compareCol))
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if row[compareCol].find(s2) != -1:
				rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on commas
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(count) == str(elem): #if the row# matches an entry in "matches"
					results+=row[1]+' '+row[2]+'\n'
			count+=1
		f.seek(0)		
			
	finally:
		f.close() 
		return results

def string_to_matches(s0,s1): #list, LANDesk,landeskname,landeskoption
	firststring = s0.split('\n')
	secondstring = s1.split('\n')
	matchedrecords=""
	output=''
	
	for elem0 in firststring:#iterate through landesk
		if str(elem0) != "" and str(elem0) != " ":
			for elem1 in secondstring:#iterate through softwaredb
				if str(elem1) != "" and str(elem1) != " ":
					temp = elem1.split(',')#split sfdb ID and name
					taken=False
					if str(elem0) == temp[1]:#if the landesk record matches the software license name
						temp1 = matchedrecords.split(',')#split the spoken-for records
						for elem2 in temp1:#for each spoken-for record
							if elem2 == temp[0]:#if it matches this software database record's id mark it as taken
								taken=True
						if taken != True:#if it's not taken
							output += str(elem0)+','+temp[0]+'|'#add it to the output (append software db id)
							matchedrecords+=temp[0]+","
	return output
	
def string_to_problem(s0,s1,s2,s3): #list, LANDesk,landeskname,landeskoption
	output=''
	
	matches = string_to_matches(s0,s1).split('|')#get the software db records
	installs = landesk_to_full_name('landesk.csv','Name',s2).split('\n')#get the list of user installs from LANDESK
	spokenforrecords=""
	count1=0
	count2=0
	valid=False
	
	for el1 in installs:#cycle through installs
		if str(el1) != "" and str(el1) != " ":
			count1+=1;
			count2=0;
			valid=False
			for el2 in matches:#cycle through licenses
				count2+=1;
				temp2 = spokenforrecords.split(',')#split the SoftwareDB IDs that we've already used up
			
				#check to see if the current install matches with a license
				temp3 = str(el2).split(',')
				if(el1 == temp3[0]):#install name vs. license name
					
					#is it taken?
					taken=False
					for elem in temp2:#if it matches with a license make sure it's not already used
						if elem != "" and elem != " ":
							if elem == temp3[1]:#it's already been used by another install so it's invalid.
								print("unfortunately that licnese is already taken by this check")
								taken=True
					
					#if it's not taken
					if taken != True:
						valid=True
						spokenforrecords+=temp3[1]+','
						
					if valid == True:
						break
		
		#if it's false at this point it failed to match ANY free record and it's invalid
		if valid == False:
			output+=str(el1)+'|'#add it to the list of problems
	print(str(count1)+" installs tested")
	print(str(count2)+" licenses tested")
	return output # the list will now only contain problem installs
	
def string_to_unused(s0,s1,s2,s3): #list, LANDesk,softwaredbname,softwaredboption
	output=''
	
	records = file_to_list('sdextract.csv','SoftwareTitle',s2,'Users',s3).split('\n') #get the software records that match
	matches = string_to_matches(s0,s1)#get the spoken for records
	matches = matches.split('|')
	
	for el1 in records:#software db records
		spokenfor=False
		if str(el1) != "" and str(el1) != " ":
			temp1 = el1.split(',')
			for el2 in matches: #landesk names + IDS
				if str(el2) != "" and str(el2) != " ":
					temp2 = el2.split(',')
					if temp1[0] == temp2[1]:#if record ID and Landesk Name+ID match it's already in use by an accurate install
						spokenfor=True
		if spokenfor == False:
			output+=str(el1)+'|'

	return output
	
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def remove_bad_chars(s0):
	badchars = "[]'"
	stringbuild=''
	
	for elem in s0:
		flag = True
		for elem1 in badchars:
			if str(elem) == str(elem1):
				flag = False
		if flag==True:
			stringbuild+= str(elem)
	
	return stringbuild
	
#Main Routine
def main(arg1,arg2,arg3,arg4):
	print('')
	print('Software Database Adjuster v1.4')
	print('________________________________________________')

	print('searching for...'+str(arg1)+' and '+str(arg3))
	landeskname= arg1
	softwaredbname= arg3
	
	#read in filtering type/allowance
	landeskoption = "explicit"
	softwaredboption = "explicit"
	if str(arg2)=="1":
		landeskoption = "similar"
	if str(arg2)=="2":
		landeskoption = "contains"
	if str(arg4)=="4":
		softwaredboption = "similar"
	if str(arg4)=="5":
		softwaredboption = "contains"
	
	#write html header
	print('1/5 - Forming Presentation Layer...')
	writestring='<!DOCTYPE html><html><head>'
	writestring+='<script src="sorttable.js"></script>'
	writestring+='<style>body{background-color: #F2F2F2;}table, td, th {border: 1px solid black;border-collapse: collapse;background-color: #D9D9D9;}td.offline{background-color: rgb(130, 206, 184);}'
	writestring+='th{background-color: #C9C9C9;border: 1px solid black;border-collapse: collapse;}#results{border: solid;text-align: center;}'
	writestring+='</style></head><body>'

	#print accurate and installed records
	print('2/5 - Find Accurate Records...')
	writestring+='<table class="sortable" style="width:100%">'
	writestring+='<h2><b>Accurate and Installed Records</b></h2>'
	writestring+='<tr><th>-#-</th><th>Device Name</th><th>First Name</th><th>Last Name</th><th>Department</th><th>Division</th><th>City</th><th>Building</th><th>Login Name</th><th>Last Hardware Scan</th><th>Disposition</th><th>Last Started</th><th>Name</th><th>Version</th></tr>'
	acc = string_to_matches(landesk_to_full_name('landesk.csv','Name',landeskname),file_to_list('sdextract.csv','SoftwareTitle',softwaredbname,'Users',softwaredboption))
	acc = str(acc).split('|')
	count0 = 1
	for elem in acc:
		p = elem.split(',')
		t = remove_bad_chars(str(p[0]))
		if t != '' and t != ' ':
			writestring+='<tr>'
			writestring+='<td valign="top"><b>'+str(count0)+'</b></td>'
			count0 +=1
			temp = landesk_to_full_list_from_name('landesk.csv','Name',landeskname,t)
			#print temp
			temp = temp.split('|')
			offlineRow=True
			for elem1 in temp:
				if str(elem1).lower().find("in service") != -1:
					offlineRow=False
			for elem1 in temp:
				if offlineRow:
					writestring+='<td class="offline" valign="top">'+str(elem1)+'</td>'
				else:
					writestring+='<td valign="top">'+str(elem1)+'</td>'
			writestring+='</tr>'
	writestring+='</table>'

	#print spare licenses
	print('3/5 - Finding Spare Licenses...')
	writestring+='<table class="sortable" style="width:100%">'
	writestring+='<h2><b>Unused Licenses</b></h2>'
	writestring+='<tr><th>-#-</th><th>ID</th><th>Users</th><th>Department</th><th>Division</th><th>Software</th><th>Version</th><th>Copies</th><th>Purchased</th><th>MS Subscription</th><th>Serial Number</th><th>Authorization Code</th><th>License ID</th><th>Contract Number</th><th>PO</th><th>Asset No.</th><th>Updated By</th><th>Edited Date</th><th>Created Date</th><th>Previous Owner</th><th>Comments</th><th>Verified Status</th></tr>'
	spareinstall = string_to_unused(landesk_to_full_name('landesk.csv','Name',landeskname),file_to_list('sdextract.csv','SoftwareTitle',softwaredbname,'Users',softwaredboption),softwaredbname,softwaredboption)
	spareinstall = str(spareinstall).split('|')
	count1=1;
	for elem in spareinstall:
		t = remove_bad_chars(str(elem))
		if t != '' and t != ' ':
			tempid = elem.split(',')
			temp = file_to_full_list('sdextract.csv','ID',tempid[0])#grab the fields based on row ID
			temp = temp.split('|')
			writestring+='<tr>'
			writestring+='<td valign="top"><b>'+str(count1)+'</b></td>'
			count1 +=1
			for elem1 in temp:
				writestring+='<td valign="top">'+elem1+'</td>'
			writestring+='</tr>'
	writestring+='</table>'
		
	#print problem installs
	print('4/5 - Finding Problem Installs...')
	writestring+='<table class="sortable" style="width:100%">'
	writestring+='<h2><b>Problem Installs</b></h2>'
	writestring+='<tr><th>-#-</th><th>Device Name</th><th>First Name</th><th>Last Name</th><th>Department</th><th>Division</th><th>City</th><th>Building</th><th>Login Name</th><th>Last Hardware Scan</th><th>Disposition</th><th>Last Started</th><th>Name</th><th>Version</th></tr>'
	probinstall = string_to_problem(landesk_to_full_name('landesk.csv','Name',landeskname),file_to_list('sdextract.csv','SoftwareTitle',softwaredbname,'Users',softwaredboption),landeskname,landeskoption).split('\n')
	probinstall = str(probinstall).split('|')
	count2=1
	for elem in probinstall:
		t = remove_bad_chars(str(elem))
		if t != '' and t != ' ':
			x=landesk_to_full_list_from_name('landesk.csv','Name',landeskname,str(t))
			x=x.split('|')
			writestring+='<tr>'
			writestring+='<td valign="top"><b>'+str(count2)+'</b></td>'
			count2 +=1
			
			for elem1 in x:
				writestring+='<td valign="top">'+elem1+'</td>'
			writestring+='</tr>'
	writestring+='</table>'

	#close the html
	writestring+="</br>"
	
	accRec = count0-1
	unuRec = count1-1
	proRec = count2-1
	
	writestring+="<div id='results'>"
	writestring+="<b>Accurate Records:"+str(accRec)+"</b></br>"
	writestring+="<b>Unused Licenses:"+str(unuRec)+"</b></br>"
	writestring+="<b>Problem Installs:"+str(proRec)+"</b></br></br>"
	if accRec>1 and unuRec>1 and proRec>1:
		writestring+="<b>Accuracy: "+str((((proRec/(accRec+unuRec))-1)*100)*-1)+"%</b></br></div>"
	print('5/5 - Completing the Report...')
	writestring+='</body></html>'

	with open('testOuptut.html','w') as the_file:
		the_file.write(writestring)
	the_file.close

	print('________________________________________________')
	print('100% Complete --- Please Review testOutput.html')
	
if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])