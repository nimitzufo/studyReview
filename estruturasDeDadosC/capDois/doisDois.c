#include <stdio.h>
#include "../ed/pilha.h"

int main(void) {
	Pilha P = pilha(100);
	empilha(8,P);
	while (topo(P)>0)
		empilha(topo(P)/2,P);
	while (!vaziap(P))
		printf("%f\n", desempilha(P));
	return 0;
}
