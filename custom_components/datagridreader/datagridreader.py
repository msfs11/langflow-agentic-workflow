# from lfx.field_typing import Data
from lfx.custom.custom_component.component import Component
from lfx.io import MessageTextInput, Output
from lfx.schema.data import Data
import pandas as pd


class DataGridReader(Component):
    display_name = "Data Grid Reader"
    description = "Reads CSV or XLSX files and outputs data as a grid"
    documentation: str = "https://docs.langflow.org/components-custom-components"
    icon = "Table"
    name = "DataGridReader"

    inputs = [
        MessageTextInput(
            name="file_path",
            display_name="File Path",
            info="Enter the path to a CSV or XLSX file",
            value="",
            tool_mode=True,
        ),
    ]
    

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        if not self.file_path:
            return Data(value=[])

        file_path = self.file_path
        try:
            if file_path.lower().endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.lower().endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file type. Please provide a CSV or XLSX file.")

            data_grid = df.to_dict('records')
            data = Data(value=data_grid)
            self.status = data
            return data
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")