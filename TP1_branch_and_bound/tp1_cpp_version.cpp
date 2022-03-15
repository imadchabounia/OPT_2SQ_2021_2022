#include<bits/stdc++.h>
using namespace std;

const float oo = (1e+9);

struct Node
{
  int32_t i;
  int32_t x;
  float profit;
  int32_t w;
  float eval;
  shared_ptr<Node> parent;
  Node(int32_t a, int32_t b, float c, int32_t d, float e, shared_ptr<Node> p): i(a), x(b), profit(c), w(d), eval(e), parent(p) {}
};

void afficher_solution(shared_ptr<Node> solution)
{
  shared_ptr<Node> node = solution;
  cout << "Max profit : " << node->profit << endl;
  while(node->i != 0 && node != nullptr)
  {
    cout << "x" << node->i << " = " << node->x << endl;
    node = node->parent;
  }
}

void branch_and_bound(const vector<pair<int32_t, int32_t>>& items, int32_t W)
{
  //solution récursive
  //W : capacité max
  stack<shared_ptr<Node>> st;
  st.push(make_shared<Node>(0, 0, 0, W, INT_MAX, nullptr));
  vector<shared_ptr<Node>> candidates;
  int32_t n = items.size();
  float M = -oo; //borne inf
  while(!st.empty())
  {
    shared_ptr<Node> top = st.top();
    st.pop();
    if(top->i == n)
    {
      candidates.push_back(top);
      M = fmaxf(M, top->profit);
    }
    else if(top->i < n)
    {
      int32_t new_w = top->w;
      int32_t new_i = top->i + 1; //next i
      int32_t xi;
      for(xi = 0; top->w-items[top->i].second*xi >= 0; xi++)
      {
        int32_t new_x = xi;
        float new_profit = top->profit + items[top->i].first*xi;
        new_w = top->w-items[top->i].second*xi;
        float new_eval = top->eval;
        shared_ptr<Node> new_parent = top;
        if(new_profit < new_eval)
        {
          st.push(make_shared<Node>(new_i, new_x, new_profit, new_w, new_eval, new_parent));
        }
      }
      if(new_w > 0)
      {

        if(new_i < n)
        {
          shared_ptr<Node> new_parent = top;
          int32_t new_x = xi;
          float new_profit = top->profit + items[top->i].first*xi;
          float new_eval = fminf(top->eval, (items[new_i].first/items[new_i].second)*new_w);
          if(new_eval > M) st.push(make_shared<Node>(new_i, new_x, new_profit, new_w, new_eval, new_parent));
        }
      }
    }
  }
  shared_ptr<Node> solution = candidates.back();
  for(auto& p : candidates)
  {
    if(p->profit > solution->profit)
    {
      solution = p;
    }
  }
  afficher_solution(solution);

}

void go(int32_t i, const vector<pair<int32_t, int32_t>>& items, float profit, int32_t W, float eval)
{
  int32_t n = items.size();
  if(W == 0 || i == (int32_t)items.size())
  {

    //cout << "Profit = " << profit << endl;
    return;
  }
  if(profit > eval) return;
  else
  {
    int32_t w = 0;
    for(int32_t xi = 0; W-items[i].second*xi >= 0; xi++)
    {
      w = W-items[i].second*xi;
      go(i+1, items, profit+items[i].first*xi, w, eval);
    }
    if (w>0)
    {
      if(i+1 < n)
      {
        float new_eval = fminf(eval, profit + (items[i+1].first/items[i+1].second)*w);
        go(i+1, items, profit, w, new_eval);
      }
    }
  }
}

int main(void)
{
  ifstream cin("testcases.txt");
  int32_t N;
  cin >> N;
  while(N--)
  {
    vector<pair<int32_t, int32_t>> items;
    int32_t n; cin >> n;
    int32_t W; cin >> W;
    vector<int32_t> a; for(int32_t i = 0; i < n; i++) { int32_t p; cin >> p; a.push_back(p);}
    vector<int32_t> b; for(int32_t i = 0; i < n; i++) { int32_t w; cin >> w; b.push_back(w);}
    for(int32_t i = 0; i < n; i++) items.push_back(make_pair(a[i], b[i]));
    auto comp = [&](const pair<int32_t, int32_t>& p1, const pair<int32_t, int32_t>& p2)
    {
      return (p1.first/p1.second) > (p2.first/p2.second);
    };
    sort(items.begin(), items.end());
    //cout << "this is recursive solution, it sucks ! (t3ayi)" << endl;
    //go(0, items, 0, W, INT_MAX);
    cout << "--------------------------------------------------------" << endl;
    branch_and_bound(items, W);
    cout << "--------------------------------------------------------" << endl;
  }
  return 0;
}
