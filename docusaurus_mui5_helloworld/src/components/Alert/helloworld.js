import * as React from "react";
import Alert from "@mui/material/Alert";
import Stack from "@mui/material/Stack";
import { Box } from "@mui/material";

export default function BasicAlerts() {
  return (
    <>
      <Box>Hello alert</Box>
      <Alert severity="error">This is an error alert — check it out!</Alert>
    </>
  );
}
