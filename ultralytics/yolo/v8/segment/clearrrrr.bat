@echo off
:: Use PowerShell to remove the contents of the detect directory
powershell -Command "Remove-Item -Path 'D:\BasicProjects\YOLOv8_Segmentation_DeepSORT_Object_Tracking\runs\detect\*' -Recurse -Force"

:: Check if the removal was successful
if exist "D:\BasicProjects\YOLOv8_Segmentation_DeepSORT_Object_Tracking\runs\detect\*" (
    echo Failed to remove all items in the directory.
) else (
    echo All items in the directory removed successfully.
)
