import json
import deepdiff


with open('1.json', 'r') as f:
        a = json.load(f)

with open('2.json', 'r') as f:
        b = json.load(f)


def compare_obj(a,b):  
    if (type(a) != type (b)):      
        return False  
    elif type(a) is dict:      
        return compare_dict(a,b)  
    elif type(a) is list:
        return compare_list(a,b)
    else:      
        return a == b
   
def compare_dict(a,b):  
    if len(a) > len(b):      
        return False  
    else:      
        for key,value in a.items():        
            if not key in b:            
                return False        
            else:            
                if not compare_obj(value, b[key]):              
                    return False  
    return True

def compare_list(a,b):  
    if len(a) > len(b):      
        return False  
    else:      
        for i in range(len(a)):        
            if not compare_obj(a[i], b[i]):            
                return False  
    return True




def compare(d1, d2, level='root'):
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            s1 = set(d1.keys())
            s2 = set(d2.keys())
            print('{:<20} + {} - {}'.format(level, s1-s2, s2-s1))
            common_keys = s1 & s2
        else:
            common_keys = set(d1.keys())

        for k in common_keys:
            compare(d1[k], d2[k], level='{}.{}'.format(level, k))

    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) != len(d2):
            #print('{:<20} len1={}; len2={}'.format(level, len(d1), len(d2)))
            ddiff=deepdiff.DeepDiff(d1,d2,ignore_order='true',verbose_level=0)
            print(ddiff)
        common_len = min(len(d1), len(d2))

        for i in range(common_len):
            compare(d1[i], d2[i], level='{}[{}]'.format(level, i))

    else:
        if d1 != d2:
            #print('{:<20} {} != {}'.format(level, d1, d2))
            ddiff=deepdiff.DeepDiff(d1,d2,ignore_order='true',verbose_level=0)
            print(ddiff)
            
            
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

def main():
    a_obj=json.dumps(a,sort_keys='True')
    b_obj=json.dumps(b,sort_keys='True')
    aordered=dict(ordered(a))
    bordered=dict(ordered(b))
    a_decoded = json.loads(a_obj)
    b_decoded = json.loads(b_obj)
    a_obj=json.dumps(a,sort_keys='True')
    b_obj=json.dumps(b,sort_keys='True')
   
    a_decoded = json.loads(a_obj)
    b_decoded = json.loads(b_obj)
    value=str(compare_obj(a_decoded, b_decoded))
    # print(value)
    if(value=="True"):
        print("json matched and extra values if any are \n")
        compare(aordered,bordered)
    elif(value=="False"):
        print("local json doesnt matches server json and differences are \n")
        compare(aordered,bordered)
if __name__ == '__main__':
    main()