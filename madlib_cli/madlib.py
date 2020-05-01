#Features
#read in a template file
# parse the template
# present choices to user
# get input from user
# inject user input into template
# Display to user
# write the completed mad lib to a file

template_string ="A {Adjective} and {Adjective} {Noun}"
result_list =[]

def parse(template):
    word_list = template.split(" ")
    i=0
    while i<=len(word_list)-1:
        list_item = word_list[i]
        if list_item[:1] == "{":
            result_list.append(list_item[1:-1])
        i+=1
    return (result_list)

def take_input(prompt_list):
    i=0
    while i<=len(prompt_list)-1:
        response = input(f"Enter text for {prompt_list[i]}")    
        result_list.append(response)
        i+=1
    return (result_list)


def inject_to_template(response_list):
    word_list = template_string.split(" ")
    result_list=[]
    finalstr=" "
    i=0
    j=0
    while i<=len(word_list)-1:
        list_item = word_list[i]
        result_list.append(word_list[i])
        if list_item[:1] == "{":
            result_list.remove(word_list[i])
            result_list.append(response_list[j])
            j+=1
        
        i+=1
    finalstr = finalstr.join(result_list)
    print(finalstr)

#parse(template_string)
inject_to_template(take_input(['Adjective','Adjective','Noun']))
inp = parse(template_string)
#inject_to_template(take_input(inp))
