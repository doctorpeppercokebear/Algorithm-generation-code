import React from "react";
import axios from "axios";
import {Form, Divider, Input,InputNumber, Button} from "antd";
import FormItem from "antd/lib/form/FormItem";

function App() {
  const [predict, setPredict] = React.useState("");
  const onSubmit = (values) => {
    let formData = new FormData();
    formData.append("temperature", values.temperature);
    formData.append("humidity", values.humidity);
    console.log("temperature:" + formData.get("temperature"));
    console.log("humidity:" + formData.get("humidity"));
    const backend_url = "http://127.0.0.1:8000/ai/";
    axios
    .post(backend_url, formData)
    .then((response) => {
      console.log(response.data["predict"]);
    })
    .catch((error) => {
      console.log(error);
    });
  };

  return <div>
    <Form name='Bechu' onFinish={onSubmit}>
      <Form.Item
        name='temperature'
        label="temperature"
        rules={[{required: true, type: 'number',  min: 0, max: 99, message: "평균기온을 입력하세요"}]}
        >
          <InputNumber placeholder="평균기온 입력" />
      </Form.Item>
       <Form.Item
        name="humidity"
        label="humidity"
        rules={[{ required: true, type: "number", min: 0, max: 99, message: "평균습도를 입력하세요." }]}
        >
          <InputNumber placeholder="평균습도 입력" />
        </Form.Item>
      <Divider />
      <div>
        <h2>예상배추가격 : {predict}</h2>
      </div>
      <Form.Item>
        <Button id="submit-button" size="large" htmlType="submit">
          배추가격예측
        </Button>
      </Form.Item>
    </Form>
  </div>;
}
  
export default App;
       
     
