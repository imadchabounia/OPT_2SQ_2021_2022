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
  int32_t index;
  shared_ptr<Node> parent;
  Node(int32_t a, int32_t b, float c, int32_t d, float e, shared_ptr<Node> p, int32_t index): i(a), x(b), profit(c), w(d), eval(e), parent(p), index(index) {}
};

void afficher_solution(shared_ptr<Node> solution)
{
  shared_ptr<Node> node = solution;
  cout << "Max profit : " << node->profit << endl;
  while(node->i != 0 && node != nullptr)
  {
    cout << "x" << node->index << " = " << node->x << endl;
    node = node->parent;
  }
}

void branch_and_bound(const vector<vector<int32_t>>& items, int32_t W)
{
  //solution récursive
  //W : capacité max
  stack<shared_ptr<Node>> st;
  st.push(make_shared<Node>(0, 0, 0, W, INT_MAX, nullptr, 0));
  //vector<shared_ptr<Node>> candidates;
  int32_t n = items.size();
  float M = -oo; //borne inf
  shared_ptr<Node> solution;
  while(!st.empty())
  {
    shared_ptr<Node> top = st.top();
    st.pop();
    if(top->i == n)
    {
      //candidates.push_back(top);
      if(top->profit > M)
      {
        solution = top;
        M = top->profit;
      }
    }
    else if(top->i < n)
    {
      int32_t new_w = top->w;
      int32_t new_i = top->i + 1; //next i
      int32_t new_index = items[top->i][2]+1;
      int32_t xi;
      for(xi = 0; top->w - items[top->i][1]*xi >= 0; xi++)
      {
        int32_t new_x = xi;
        float new_profit = top->profit + items[top->i][0]*xi;
        new_w = top->w - items[top->i][1]*xi;
        float new_eval = top->eval;
        shared_ptr<Node> new_parent = top;
        //if(new_profit <= top->eval)
        //{
          if(new_i < n)
          {
            shared_ptr<Node> new_parent = top;
            float eval_possible = (float )((float )new_profit + ((float )items[new_i][0]/(float )items[new_i][1])*(float )new_w);
            new_eval = (float )fminf(top->eval, eval_possible);
            if(new_eval >= M) st.push(make_shared<Node>(new_i, new_x, new_profit, new_w, new_eval, new_parent, new_index));
          }
          else
          {
            st.push(make_shared<Node>(new_i, new_x, new_profit, new_w, top->eval, new_parent, new_index));
          }
        //}
      }
    }
  }

  afficher_solution(solution);
}

int main(void)
{
  ifstream cin("testcases.txt");
  int32_t N;
  cin >> N;
  while(N--)
  {
    vector<vector<int32_t>> items;
    int32_t n; cin >> n;
    int32_t W; cin >> W;
    vector<int32_t> a; for(int32_t i = 0; i < n; i++) { int32_t p; cin >> p; a.push_back(p);}
    vector<int32_t> b; for(int32_t i = 0; i < n; i++) { int32_t w; cin >> w; b.push_back(w);}
    for(int32_t i = 0; i < n; i++) items.push_back(vector<int32_t>{a[i], b[i], i});
    auto comp = [&](const vector<int32_t>& p1, const vector<int32_t>& p2)
    {
      return (float )((float )p1[0]/(float )p1[1]) > (float )((float )p2[0]/(float )p2[1]);
    };
    sort(items.begin(), items.end(), comp);
    cout << "--------------------------------------------------------" << endl;
    branch_and_bound(items, W);
    cout << "--------------------------------------------------------" << endl;
  }
  return 0;
}
