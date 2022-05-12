import React from "react";
import { ThemeProvider, createTheme } from "@mui/material";

export default function TestTheme({ children }) {
  let theme = createTheme({ palette: { primary: { main: "#f00" } } });
  return (
    <>
      <ThemeProvider theme={theme}>{children}</ThemeProvider>
    </>
  );
}
