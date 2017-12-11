#include <sys/types.h>
//for windows
/*
#include <winsock2.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include "unistd.h"
*/
// for UNIX, Linux
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

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
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

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
      sleep(1);
      sts.clear();
    }
    // socketの終了
    close(sock);
  }

 return 0;
}
