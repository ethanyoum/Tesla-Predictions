import plotly.express as px
import plotly.graph_objects as go

def predictions_plot(y_train_pred,y_test_pred, model_name):
  y_train_pred = scaler.inverse_transform(y_train_pred.detach().numpy())

  # Shift train predictions for plotting
  trainPredictPlot = np.empty_like(price)
  trainPredictPlot[:, :] = np.nan
  trainPredictPlot[window:len(y_train_pred) + window, :] = y_train_pred

  # Shift test predictions for plotting
  testPredictPlot = np.empty_like(price)
  testPredictPlot[:, :] = np.nan
  testPredictPlot[len(y_train_pred) + window - 1:len(price) - 1, :] = y_test_pred

  original = scaler.inverse_transform(price['Close'].values.reshape(-1, 1))
  predictions = np.append(trainPredictPlot, testPredictPlot, axis = 1)
  predictions = np.append(predictions, original, axis = 1)
  result = pd.DataFrame(predictions)

  fig = go.Figure()
  fig.add_trace(go.Scatter(go.Scatter(x=data['Date'], y=result[0],
                    mode='lines',
                    name='Train prediction')))
  fig.add_trace(go.Scatter(x=data['Date'], y=result[1],
                    mode='lines',
                    name='Test prediction'))
  fig.add_trace(go.Scatter(go.Scatter(x=data['Date'], y=result[2],
                    mode='lines',
                    name='Actual Value')))
  fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2
    ),
    yaxis=dict(
        title_text='Close (USD)',
        titlefont=dict(
            family='Rockwell',
            size=12,
            color='white',
        ),
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Rockwell',
            size=12,
            color='white',
        ),
    ),
    showlegend=True,
    template = 'plotly_dark'

  )

  annotations = []
  annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Tesla Stock Price Change ('+ model_name + ')',
                              font=dict(family='Rockwell',
                                        size=26,
                                        color='white'),
                              showarrow=False))
  fig.update_layout(annotations=annotations)

  fig.show()

RNN_pred_plot = predictions_plot(rnn_train_pred,rnn_test_pred,'RNN')
LSTM_pred_plot = predictions_plot(lstm_train_pred, lstm_test_pred, 'LSTM')
GRU_pred_plot = predictions_plot(gru_train_pred, gru_test_pred, 'GRU')
CM_pred_plot = predictions_plot(cm_train_pred, cm_test_pred, 'CM')
