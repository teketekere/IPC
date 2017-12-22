// for UNIX, Linux
// need -std=c++11 option
#include <sys/socket.h>
#include <arpa/inet.h>
#include <cstring>
#include <sstream>
#include <unistd.h>

class SocketClient
{
private:
  int sock;
  struct sockaddr_in server;

public:
  // hostを指定しない場合はローカルホストにつなぐ
  SocketClient(unsigned short portnum)
  {
    // ソケットの作成
    this->sock = socket(AF_INET, SOCK_STREAM, 0);
    // create structure for socket communication
    this->server.sin_family = AF_INET;
    this->server.sin_port = htons(portnum);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    // this->server.sin_addr.s_addr = inet_addr("192.168.1.1");
  }

  SocketClient(std::string hostip, unsigned short portnum)
  {
    // ソケットの作成
    this->sock = socket(AF_INET, SOCK_STREAM, 0);
    // create structure for socket communication
    this->server.sin_family = AF_INET;
    this->server.sin_port = htons(portnum);
    this->server.sin_addr.s_addr = inet_addr(hostip.c_str());
  }

  ~SocketClient()
  {
    this->closeClient();
  }

  void connectServer()
  {
    try
    {
      connect(this->sock, (struct sockaddr *)&(this->server), sizeof(this->server));
    }
    catch(...)
    {
      throw;
    }
  }

  void senddata(std::string data)
  {
    std::stringstream sts;
    std::string str;
    str = data;
    char sdata[64];
    sts <<  str;
    sts >> sdata;
    const char* sdataconst = sdata;
    write(this->sock, sdataconst, strlen(sdataconst));
    sts.clear();
  }

  void closeClient()
  {
    try
    {
      close(this->sock);
    }
    catch(...)
    {
      throw;
    }
  }
};

int main()
{
  // Code for debug
  SocketClient *client = new SocketClient("192.168.1.1", 19001);
  client->connectServer();
  int count = 0;
  while(1)
  {
    std::string senddata = (count < 10) ? std::to_string(count) : "end";
    client->senddata(senddata);
    usleep(1000000);
    if(count >= 10) break;
    count++;
  }
  delete(client);
  return 0;
}
