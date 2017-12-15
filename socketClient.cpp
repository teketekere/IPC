// for UNIX, Linux
#include <sys/socket.h>
#include <arpa/inet.h>
#include <cstring>
#include <sstream>
#include <unistd.h>

int main()
{
  int sockmode = 1;
  if(sockmode == 1)
  {
    struct sockaddr_in server;
    int sock;
    char buf[64];
    int n;

    // ソケットの作成
    sock = socket(AF_INET, SOCK_STREAM, 0);
    // create structure for socket communication
    server.sin_family = AF_INET;
    server.sin_port = htons(19001);
    // server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_addr.s_addr = inet_addr("192.168.1.1");

    // connect to server
    connect(sock, (struct sockaddr *)&server, sizeof(server));

    int count = 0;
    while(1)
    {
      memset(buf, 0, sizeof(buf));
      std::stringstream sts;
      std::string str;
      if(count < 10)
      {
        str = std::to_string(count);
        count++;
      }
      else
      {
        str = "end";
      }

      char sdata[64];
      sts <<  str;
      sts >> sdata;
      const char* sdataconst = sdata;
      write(sock, sdataconst, strlen(sdataconst));
      usleep(1000000);
      sts.clear();
    }
    // socketの終了
    close(sock);
  }

 return 0;
}
