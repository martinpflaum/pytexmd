__all__ = ["get_number_within_equation","has_value_equal"]

from . import splitting

def get_number_within_equation(string:str)->str:
    string = string.split("\\numberwithin{equation}")
    if len(string) == 1:
        return "document" 
    out,_ = splitting.split_on_first_brace(string[1])
    return out

def has_value_equal(instance, attribute_name:str, value) -> bool:
    if instance.hasattr(attribute_name):
        return (object.__getattribute__(instance,attribute_name)==value)
    else:
        return False


"""
def convert_latex(string,all_classes_prio):
    if not isinstance(all_classes_prio[0],list):
        all_classes_prio = [all_classes_prio]

    string = antibugs.no_more_bugs_begin(string)
    string = do_commands(string)
    string = do_newenvironment(string)
    all_classes_prio[0].extend(get_theoremSearchers(string))
    number_within_equation = get_number_within_equation(string)
    

    pre_docmuent,document,post_document = Document.split_and_create(string,None)
    document.globals.number_within_equation = number_within_equation
    
    for expand_on in all_classes_prio:
        document.expand(expand_on)
    document.expand([JunkSearch("{",save_split=False),JunkSearch("}",save_split=False)])
    document.expand([JunkSearch("\\ ",save_split=False)])
    
    
    #pre_content are just commands
    print("processing finished! now the final file will be created.")
    document._finish_up()
    out = document.to_string(tab_lvl=0)
    out = antibugs.no_more_bugs_end(out)    
    
    return out

"""