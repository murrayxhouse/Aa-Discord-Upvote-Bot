import base64

def tokenEncrypt(run,tokens):
    if(run==True):
        for x in range(len(tokens)):
            with open(tokens[x][0:2]+"_"+str(x)+".b64","wb") as file:
                tokens[x]=base64.encodestring(tokens[x].encode("utf-8"))
                print(tokens[x])
                file.write(tokens[x])
    print("Tokens encrpyted\n----")
tokenEncrypt(True,["Mzc2Njg5NzE0NDg2NDQ0MDMz.DRxC9w.9oXaYdvqFZT6UoN1Y7nnF_uKZxk","NDM1MDY1ODA3OTc0OTU3MDU2.Db_dmg.M95QMQq4PR3FgHvvaRevbexHKVg"])
