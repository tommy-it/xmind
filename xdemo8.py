from xmindparser import xmind_to_dict

xmind_file = 'test.xmind'

xmind_dict = xmind_to_dict(xmind_file)


def count_titles_and_tags(topics):
    """
    递归地统计所有的title和tag数量
    """
    title_count = len(topics)  # 统计当前主题块的数量
    tag_red_count = 0
    tag_orange_count = 0
    tag_green_count = 0

    for topic in topics:
        if 'makers' in topic and 'tag-red' in topic['makers']:
            tag_red_count += 1
        if 'makers' in topic and 'tag-yellow' in topic['makers']:
            tag_orange_count += 1
        if 'makers' in topic and 'tag-green' in topic['makers']:
            tag_green_count += 1

        if 'topics' in topic:
            sub_topics = topic['topics']
            sub_counts = count_titles_and_tags(sub_topics)
            title_count += sub_counts[0]
            tag_red_count += sub_counts[1]
            tag_orange_count += sub_counts[2]
            tag_green_count += sub_counts[3]

    return title_count, tag_red_count, tag_orange_count, tag_green_count


# 统计所有的title和tag数量
# total_counts = count_titles_and_tags(xmind_dict[0]['topic']['topics'])
# print("Total number of titles:", total_counts[0])
# print("Total number of tag-red:", total_counts[1])
# print("Total number of tag-orange:", total_counts[2])
# print("Total number of tag-green:", total_counts[3])


# for canvas in xmind_dict:
#     print("Canvas name:", canvas['title'])
#     topics = canvas['topic']['topics']
#     total_counts = count_titles_and_tags(topics)
#     print("Total number of titles in canvas:", total_counts[0])
#     print("Total number of tag-red in canvas:", total_counts[1])
#     print("Total number of tag-orange in canvas:", total_counts[2])
#     print("Total number of tag-green in canvas:", total_counts[3])


# 初始化总计数器
total_counts = [0, 0, 0, 0]  # title计数器，tag-red计数器，tag-orange计数器，tag-green计数器

for canvas in xmind_dict:
    print("Canvas name:", canvas['title'])
    topics = canvas['topic']['topics']
    canvas_counts = count_titles_and_tags(topics)
    print("Total number of titles in canvas:", canvas_counts[0])
    print("Total number of tag-red in canvas:", canvas_counts[1])
    print("Total number of tag-orange in canvas:", canvas_counts[2])
    print("Total number of tag-green in canvas:", canvas_counts[3])

    # 累加计数器
    total_counts[0] += canvas_counts[0]  # title计数器累加
    total_counts[1] += canvas_counts[1]  # tag-red计数器累加
    total_counts[2] += canvas_counts[2]  # tag-orange计数器累加
    total_counts[3] += canvas_counts[3]  # tag-green计数器累加

# 输出总计数器结果
print("Canvas name:总计数")
print("Total number of titles:", total_counts[0])
print("Total number of tag-red:", total_counts[1])
print("Total number of tag-orange:", total_counts[2])
print("Total number of tag-green:", total_counts[3])