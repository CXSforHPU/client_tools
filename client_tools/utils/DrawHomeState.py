from termgraph.module import Data, BarChart, Args, Colors
from client_tools.chat_client.GetHomeState import getHomeState
from client_tools.utils.LoadConfig import LoadHomeState

def DrawHomeStateCMD(num=10):
    getHomeState("./data.yml")
    tim,tem,hum = LoadHomeState("./data.yml",num)
    data = Data([[tem, hum] for tem,hum in zip(tem,hum)],tim, ["tem", "hum"])
    chart = BarChart(
        data,
        Args(
            title="Total Marks Per Class",
            colors=[Colors.Red, Colors.Magenta],
            space_between=True,
        ),
    )

    chart.draw()



if __name__ == "__main__":
    DrawHomeStateCMD()

