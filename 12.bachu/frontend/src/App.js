import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from "axios";
import {Form, Divider, InputNumber, Button} from "antd";

function App() { 
    const [predict, setPredict] = React.useState(0);
    const onSubmit = (values) =>{
      console.log(values);
      let formData = new FormData();
      formData.append("temperature", values.temperature);
      formData.append("humidity", values.humidity);
      const url = "http://192.168.0.54:8000/api/ai";
      axios.post(url, formData).then((response) => {setPredict(response.data.predict);}).catch((error) => {console.log(error);});
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <div>
        <Form name= "ai" onFinish={onSubmit}>
          <Form.Item
           name="temperature"
           label={<div id="temperature"> 평균기온</div>}
           rules={[{ required: true, type:'number', 
           min:-99,
           max:99, }]}>
            <InputNumber />   
        </Form.Item>
        <Form.Item
           name="humidity"
           label={<div id="humidity"> 평균습도</div>}
           rules={[{ required: true, type:'number', 
           min:-99,
           max:99, }]}>
            <InputNumber />
          </Form.Item>
        <Divider />
        <div>
          <h2>예상 배추 가격: {predict}</h2>
        </div>
        <Form.Item>
          <Button type="primary" size="large" htmlType='submit'>
            예측하기
          </Button>
          </Form.Item>
        </Form>
        </div>  
    </div>
  );
}

export default App;
