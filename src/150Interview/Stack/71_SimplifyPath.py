class Solution:
    def simplifyPath(self, path: str) -> str:
        last_folders: list[str] = []
        current_folder_name = ""
        path += "/"

        for character in path:
            if character == "/":
                if current_folder_name == "":
                    continue
                elif current_folder_name == ".":
                    current_folder_name = ""
                    continue
                elif current_folder_name == "..":
                    if len(last_folders) != 0:
                        last_folders.pop()
                else:
                    last_folders.append(current_folder_name)
                current_folder_name = ""
                continue
            current_folder_name += character

        return "/" + "/".join(last_folders)


print(Solution().simplifyPath("/a//b////c/d//././/.."))
