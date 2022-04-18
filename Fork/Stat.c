#include<stdio.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<stdlib.h>

int main()
{
  //pointer to stat struct
  struct stat sfile;

  //stat system call
  stat("statcall.c", &sfile);

  //accessing st_mode (data member of stat struct)  
  printf("st_mode = %o", sfile.st_mode);

  printf("\nFile st_uid %d \n",sfile.st_uid); //user id
  printf("\nFile st_blksize %ld \n",sfile.st_blksize); //gives preferred block size
  printf("\nFile st_gid %d \n",sfile.st_gid); //group id
  printf("\nFile st_blocks %ld \n",sfile.st_blocks); //total number of blocks in multiples of 512 bytes
  printf("\nFile st_size %ld \n",sfile.st_size); //size of the file
  printf("\nFile st_nlink %u \n",(unsigned int)sfile.st_nlink); //total number of hard links
  printf("\nFile st_dev %d \n",(int)sfile.st_dev); //ID of device

  return 0;
}