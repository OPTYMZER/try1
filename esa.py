from pypresence import Presence
import time

client_id = '822199997147775038'
RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state="Duo (ItzMarkezza)", details="Playing Fortnite", large_image="xd", small_image="", large_text="Jerking", start=time.time()))

while True: 
    time.sleep(15) 