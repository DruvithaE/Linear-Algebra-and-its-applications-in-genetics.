import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def calculate_pqr(p0, q0, r0, n):
    pn = 1 - (1/2)**n * q0 - (1/2)**(n-1) * r0
    qn = (1/2)**n * q0 + (1/2)**(n-1) * r0
    rn = 0
    return pn, qn, rn

# Example usage
p0 = 0.5
q0 = 0.3
r0 = 0.2
n = 10

generation = np.arange(n + 1)
p_values = []
q_values = []
r_values = []

for i in range(n + 1):
    p, q, r = calculate_pqr(p0, q0, r0, i)
    p_values.append(p)
    q_values.append(q)
    r_values.append(r)

fig = go.Figure()
fig.add_trace(go.Scatter(x=generation, y=p_values, mode='lines+markers', name='p'))
fig.add_trace(go.Scatter(x=generation, y=q_values, mode='lines+markers', name='q'))
fig.add_trace(go.Scatter(x=generation, y=r_values, mode='lines+markers', name='r'))

fig.update_layout(
    title='Probability Dynamics',
    xaxis_title='Generation',
    yaxis_title='Probability',
    showlegend=True,
    legend=dict(x=0.9, y=0.9),
    height=500,
    width=800
)

pio.write_image(fig, 'graph.png')