#include <stdio.h>
int main() {
  int i, j;
  scanf("%d",&i);
  scanf("%d",&j);
  while (i != j) {
    if (i > j) i = i - j;
    else j = j - i;
  }
  printf("GCD = %d\n",i);
}
