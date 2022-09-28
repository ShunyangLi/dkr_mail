import React, { Component } from "react";
import "@/style/view-style/index.scss";
import CustomBreadcrumb from "../../components/CustomBreadcrumb";
import { Button, Form, Icon, message, Select, DatePicker } from "antd";
import axios from "@/api";
import { API } from "@/api/config";
import "./index.scss";

const { RangePicker } = DatePicker;
const { Option } = Select;

const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 8 }
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 16 }
  }
};

class Index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      children: [],
      date: []
    };
  }

  componentDidMount() {
    // fetch the user list for xx
    axios
      .get(`${API}/user/get-user`, {})
      .then(res => {
        let temp = [];
        res.data.names.forEach(name => {
          temp.push(<Option key={name}>{name}</Option>);
        });
        this.setState({
          children: temp
        });
      })
      .catch(function(error) {
        message.error(error.message);
      });
  }

  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        console.log("Received values of form: ", values);

        const formData = new FormData();
        formData.append("nstudents", values.next.join(","));
        formData.append("nnstudents", values.nnext.join(","));
        formData.append("ndate", this.state.date[0]);
        formData.append("nndate", this.state.date[1]);

        axios
          .post(`${API}/user/send`, formData, {})
          .then(res => {
            message.success(res.data.message);
          })
          .catch(function(error) {
            message.error(error.message);
          });
      }
    });
  };
  onFinishFailed = errorInfo => {
    console.log("Failed:", errorInfo);
  };

  dateChange = (date, dateString) => {
    this.setState({
      date: dateString
    });
  };

  render() {
    const { getFieldDecorator } = this.props.form;
    const { children } = this.state;
    return (
      <div className="content">
        <div>
          <CustomBreadcrumb arr={["mail"]} />
        </div>

        <Form
          name="basic"
          labelCol={{
            span: 24
          }}
          wrapperCol={{
            span: 16
          }}
          {...formItemLayout}
          onSubmit={this.handleSubmit}
        >
          <Form.Item label="Next Week" name="next">
            {getFieldDecorator("next", {
              rules: [
                {
                  required: true,
                  message: "Please select next week presenters"
                }
              ]
            })(
              <Select
                mode="multiple"
                placeholder="Please select next week presenters"
                onChange={this.handleChange}
                style={{
                  width: "450px"
                }}
              >
                {children}
              </Select>
            )}
          </Form.Item>

          <Form.Item label="Next Next Week" name="nnext">
            {getFieldDecorator("nnext", {
              rules: [
                {
                  required: true,
                  message: "Please select next next week presenters"
                }
              ]
            })(
              <Select
                mode="multiple"
                placeholder="Please select next next week presenters"
                onChange={this.handleChange}
                style={{
                  width: "450px"
                }}
              >
                {children}
              </Select>
            )}
          </Form.Item>

          <Form.Item label="Present Date" name="time">
            {/* can use initialValue */}
            {getFieldDecorator("time", {
              rules: [{ required: true, message: "Please select present date" }]
            })(
              <RangePicker
                format={"MM/DD/YYYY"}
                style={{
                  width: "450px"
                }}
                onChange={this.dateChange}
              />
            )}
          </Form.Item>

          <Form.Item
            wrapperCol={{
              offset: 8,
              span: 16
            }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default Form.create()(Index);
