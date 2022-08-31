import asyncio
import pprint
from pyecodevices import EcoDevices

pp = pprint.PrettyPrinter(indent=4)

async def main():
    async with EcoDevices('192.168.1.7', '80', "username", "password") as ecodevices:
        #await ecodevices.get_info()
        #print("firmware version:", ecodevices.version)
        data = await ecodevices.global_get()
        #print("all values:", data)
        #pp.pprint(data)

        HP = round(int(data["T1_HCHP"])/1000)
        HC = round(int(data["T1_HCHC"])/1000)
        print("index_heures_pleines", HP)
        print("index_heures_creuses", HC)

        t1_data = await ecodevices.get_t1()
        print("teleinfo 1:", t1_data)
        print("current:", t1_data["current"], "VA")

        data = await ecodevices.get_c1()
        print("Counter 1:", data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

