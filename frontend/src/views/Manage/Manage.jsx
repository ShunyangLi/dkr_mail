import React, { Component } from "react";
import { Card } from "antd";
import CustomBreadcrumb from "../../components/CustomBreadcrumb";

class Manage extends Component {
  render() {
    return (
      <div>
        <CustomBreadcrumb arr={["manage"]} />
        <div style={{ width: "100%" }}>
          <Card
            style={{
              width: "80%",
              margin: "auto",
              fontSize: "1.25em",
              padding: "36px"
            }}
          >
            {" "}
            <p>
              The database research group has been consistently providing the
              best research and industrial support within and beyond Australia.
              As data become big in all types of computing applications, the
              charter and collaborations of the group are expanding at the same
              time. Our research covers new challenges in data management, as
              well as big data-centric approaches to diverse areas, with
              particular emphasis on issues towards graph, multimedia,
              spatial-temporal, stream, string/textual, and uncertain data. The
              group has received various supports from the Australia Research
              Council (ARC), industry partners and research institutions such as
              CSIRO, NICTA, etc.
            </p>{" "}
          </Card>
        </div>
      </div>
    );
  }
}

export default Manage;
