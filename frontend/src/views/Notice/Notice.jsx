import React, { Component } from "react";
import {Select, Form, Button} from "antd";
import CustomBreadcrumb from "@/components/CustomBreadcrumb/CustomBreadcrumb";

const { Option } = Select;
const children = [];
for (let i = 10; i < 36; i++) {
  children.push(<Option key={i.toString(36) + i}>{i.toString(36) + i}</Option>);
}


class Notice extends Component {
  constructor(props) {
    super(props);
    this.state = {
      visible: false
    };
  }

  handleSizeChange = e => {
    this.setState({ size: e.target.value });
  };

  render() {
    const { getFieldDecorator } = this.props.form;
    return (
      <div>
        <CustomBreadcrumb arr={["send notice"]} />
        <div style={{ width: "90%", marginTop: "5%", margin: "auto", top: 2, bottom: 0, left: 0, right: 0}}>
          <Select
              mode="multiple"
              placeholder="Please select"
              defaultValue={['a10', 'c12']}
              onChange={this.handleSizeChange}
              style={{ width: '50%', marginLeft: "15%" }}
          >
            {children}
          </Select>

          <div style={{marginLeft: "15%", marginTop: "2%" }}>
            <Button type={"primary"}> Submit</Button>
          </div>
        </div>
      </div>
    );
  }
}

export default Form.create()(Notice);
