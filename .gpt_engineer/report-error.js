export const loadReportErrorEventListener = (() => {
  let isInitialized = false;

  const extractError = ({ message, lineno, colno, filename, error }) => {
    return { message, lineno, colno, filename, stack: error?.stack };
  };

  return () => {
    if (isInitialized) return;

    const reportedErrors = new Set();

    const generateErrorId = (event) => {
      const { lineno, colno, filename, message } = event;
      return `${message}|${filename}|${lineno}|${colno}`;
    };

    const isErrorAlreadyReported = (errorId) => {
      if (reportedErrors.has(errorId)) {
        return true;
      }
      reportedErrors.add(errorId);
      // Optionally, clear the set after some time to prevent it from growing indefinitely
      setTimeout(() => reportedErrors.delete(errorId), 5000);
      return false;
    };

    /**
     * Listen to runtime errors and report them to the parent window
     */
    const reportError = (event) => {
      const errorId = generateErrorId(event);

      // Prevent error being reported multiple times
      if (isErrorAlreadyReported(errorId)) {
        return;
      }

      const error = extractError(event);

      console.log("GOTERR EVENT", event);
      console.log("GOTERR ", error);

      window.top.postMessage(
        { type: "RUNTIME_ERROR", error },
        "https://run.gptengineer.app"
      );
      window.top.postMessage(
        { type: "RUNTIME_ERROR", error },
        "http://localhost:3000"
      );
    };

    window.addEventListener("error", reportError);
    isInitialized = true;
  };
})();
