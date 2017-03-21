import xml.dom.minidom

def main():
  doc=xml.dom.minidom.parse("samplexml.xml");
  
  print(doc.nodeName)
  print("Node name: ",doc.firstChild.tagName)
  
  skills=doc.getElementsByTagName("skill")
  print("%d skills: "%skills.length)
  
  couter=0
  for skill in skills:
    couter+=1
    print("Skill #",couter,"-",skill.getAttribute("name"))

  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name","javascript")
  
  doc.firstChild.appendChild(newSkill)
  
  skills=doc.getElementsByTagName("skill")
  print("%d skills: " %skills.length)
  
  
  couter=0
  for skill in skills:
    couter+=1
    print("Skill #",couter,"-",skill.getAttribute("name"))

main()
  