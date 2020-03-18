// ConsoleApplication1_3.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream> 
#include <functional>
#include <vector>
#define _CRT_SECURE_NO_WARNINGS


int main(){
	int n, s; //input data, n - number of people in the company, s - a specific number of person

	scanf_s("%d %d", &n, &s); //input data entry
	std::vector<std::vector<int>> isFriend(1 + n, std::vector<int>(1 + n));
	for (int i = 1; i <= n; i++){
		for (int j = 1; j <= n; j++){
			int v;
			scanf_s("%d", &v);
			isFriend[i][j] = (v == 1);
		}
	}
	std::vector<int> visited(1 + n, false);
	int ans = 0;
	std::function<void(int)> visit = [&](int cur){
		if (visited[cur]){
			return;
		}
		visited[cur] = true;
		ans++;
		for (int v = 1; v <= n; v++){
			if (isFriend[cur][v]){
				visit(v);
			}
		}};
	visit(s);
	printf("%d", ans - 1);
	return 0;
	
}