import json

# json: perfect
class PipelineJson(object):
    def open_spider(self, spider):
        self.f = open(spider.name + '.json', 'w')
        self.f.write('[\n')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.seek(-3 if self.f.tell() > 3 else -2, 2)
        self.f.write('\n]')
        self.f.close()